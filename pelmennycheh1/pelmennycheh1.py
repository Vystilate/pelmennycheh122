 # --- III. Подготовка фарша ---
    if a_f is not None:
        a_f_frac = a_f / 100
        P_tl_meat = P_tl_pelmeni * a_f_frac
    else:
        total_frac = (a_m + a_y + a_s + a_sp) / 100
        P_tl_meat = P_tl_pelmeni * total_frac

    n_k = math.ceil(P_tl_meat / r_k)

    return n_pa, n_tm, n_k
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

