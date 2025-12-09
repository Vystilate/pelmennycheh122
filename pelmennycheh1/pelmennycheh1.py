import math

def calculate_pelmeni_line(
    Qsut,   # суточная выработка, т
    t,      # продолжительность смены, ч
    a_t,    # массовая доля теста, %
    r_pa,   # производительность пельменного автомата, т/ч
    r_tm,   # производительность тестомесильной машины, т/ч
    r_k,    # производительность куттера, т/ч
    a_f=None, a_m=None, a_y=None, a_s=None, a_sp=None  # если нужно компонентно
):
    """
    Возвращает:
    n_pa — количество пельменных автоматов
    n_tm — количество тестомесильных машин
    n_k  — количество куттеров
    """

    # --- I. Производство пельменей ---
    P_tl_pelmeni = Qsut / (2 * t)

    n_pa = math.ceil(P_tl_pelmeni / r_pa)

    # --- II. Подготовка теста ---
    a_t_frac = a_t / 100
    P_tl_dough = P_tl_pelmeni * a_t_frac

    n_tm = math.ceil(P_tl_dough / r_tm)

if __name__ == "__main__":
    Qsut = float(input("Qсут (т/сут): "))
    t = float(input("t (ч): "))
    a_t = float(input("Ат (массовая доля теста, %): "))
    r_pa = float(input("Pпа (т/ч): "))
    r_tm = float(input("Pтм (т/ч): "))
    r_k = float(input("Pк (т/ч): "))
    a_f = float(input("Aф (%): "))

    n_pa, n_tm, n_k = calculate_pelmeni_line(
        Qsut, t, a_t, r_pa, r_tm, r_k, a_f=a_f
    )

    print("\nРЕЗУЛЬТАТЫ:")
    print(f"Пельменные автоматы: {n_pa}")
    print(f"Тестомесильные машины: {n_tm}")
    print(f"Куттеры: {n_k}")
