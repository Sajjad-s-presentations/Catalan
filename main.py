import numpy as np

# ---------------------------
# تنظیمات اولیه
# ---------------------------
num_vertices_total = 25  # تعداد کل رئوس در مجموعه
num_vertices_graph = 11  # تعداد رئوس در گراف
num_agents = 20  # تعداد عامل‌ها
max_iter = 100  # حداکثر تعداد تکرار
G_initial = 100  # مقدار اولیه ثابت گرانشی
epsilon = 1e-5  # برای جلوگیری از تقسیم بر صفر

# ایجاد ماتریس وزن تصادفی برای یال‌ها (ماتریس وزن گراف دلخواه)
np.random.seed(42)  # برای بازتولیدپذیری
adjacency_matrix = np.random.randint(1, 10, size=(num_vertices_graph, num_vertices_graph))
np.fill_diagonal(adjacency_matrix, 0)  # وزن یال‌های خود به خود صفر است

# ایجاد ماتریس وزن تخصیص (ارتباط بین رئوس اصلی و گراف)
weights_matrix = np.random.randint(1, 10, size=(num_vertices_total, num_vertices_graph))


# ---------------------------
# توابع کمکی
# ---------------------------
def fitness(solution, adjacency_matrix, weights_matrix):
    """
    محاسبه برازندگی یک راه‌حل.
    - solution: لیستی از اندیس‌های انتخاب‌شده از مجموعه 25 رأسی.
    - adjacency_matrix: ماتریس وزن یال‌های گراف.
    - weights_matrix: ماتریس وزن تخصیص.
    """
    total_weight = 0
    for i in range(num_vertices_graph):
        for j in range(num_vertices_graph):
            if i != j:  # یال‌ها باید بین دو رأس مختلف باشند
                weight = adjacency_matrix[i, j] * weights_matrix[solution[i], i] * weights_matrix[solution[j], j]
                total_weight += weight
    return total_weight


def calculate_mass(fitnesses):
    """محاسبه جرم عامل‌ها بر اساس برازندگی آن‌ها"""
    f_min = min(fitnesses)
    f_max = max(fitnesses)
    if f_min == f_max:
        return np.ones(len(fitnesses))
    return (fitnesses - f_min) / (f_max - f_min)


def calculate_gravitational_force(agent1, agent2, mass1, mass2, G):
    """محاسبه نیروی جاذبه میان دو عامل"""
    distance = np.linalg.norm(agent1 - agent2) + epsilon
    return G * (mass1 * mass2) / distance


def update_position(agent, force, num_vertices_total):
    """به‌روزرسانی موقعیت عامل"""
    new_agent = agent + force
    new_agent = np.clip(new_agent, 0, num_vertices_total - 1)  # محدود کردن به دامنه اندیس‌ها
    new_agent = np.round(new_agent).astype(int)  # مقادیر را به نزدیک‌ترین عدد صحیح گرد کنیم
    return np.unique(new_agent)[:num_vertices_graph]  # یکتا کردن و محدود کردن به تعداد رئوس گراف


# ---------------------------
# حلقه اصلی الگوریتم
# ---------------------------
# ایجاد عامل‌های تصادفی اولیه
agents = [np.random.choice(num_vertices_total, num_vertices_graph, replace=False) for _ in range(num_agents)]
best_fitness = float('-inf')
best_solution = None

for iteration in range(max_iter):
    # محاسبه برازندگی هر عامل
    fitnesses = np.array([fitness(agent, adjacency_matrix, weights_matrix) for agent in agents])

    # پیدا کردن بهترین راه‌حل فعلی
    if max(fitnesses) > best_fitness:
        best_fitness = max(fitnesses)
        best_solution = agents[np.argmax(fitnesses)]

    # محاسبه جرم عامل‌ها
    masses = calculate_mass(fitnesses)

    # ثابت گرانشی در این مرحله
    G = G_initial * (1 - iteration / max_iter)

    # محاسبه نیرو و به‌روزرسانی موقعیت عامل‌ها
    new_agents = []
    for i, agent in enumerate(agents):
        total_force = np.zeros(num_vertices_graph)
        for j, other_agent in enumerate(agents):
            if i != j:
                force = calculate_gravitational_force(agent, other_agent, masses[i], masses[j], G)
                total_force += force
        new_agent = update_position(agent, total_force, num_vertices_total)
        new_agents.append(new_agent)

    # به‌روزرسانی عامل‌ها
    agents = new_agents

    # چاپ بهترین نتیجه در هر مرحله
    print(f"Iteration {iteration + 1}: Best Fitness = {best_fitness}")

# ---------------------------
# نمایش نتیجه نهایی
# ---------------------------
print("\nBest Solution (Selected Vertices):", best_solution)
print("Best Fitness (Total Weight):", best_fitness)
