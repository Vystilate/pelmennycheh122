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

# --- III. Ïîäãîòîâêà ôàðøà ---
    if a_f is not None:
        a_f_frac = a_f / 100
        P_tl_meat = P_tl_pelmeni * a_f_frac
    else:
        total_frac = (a_m + a_y + a_s + a_sp) / 100
        P_tl_meat = P_tl_pelmeni * total_frac

    n_k = math.ceil(P_tl_meat / r_k)

    return n_pa, n_tm, n_k
if __name__ == "__main__":
    Qsut = float(input("Qñóò (ò/ñóò): "))
    t = float(input("t (÷): "))
    a_t = float(input("Àò (ìàññîâàÿ äîëÿ òåñòà, %): "))
    r_pa = float(input("Pïà (ò/÷): "))
    r_tm = float(input("Pòì (ò/÷): "))
    r_k = float(input("Pê (ò/÷): "))
    a_f = float(input("Aô (%): "))

    n_pa, n_tm, n_k = calculate_pelmeni_line(
        Qsut, t, a_t, r_pa, r_tm, r_k, a_f=a_f
    )

    print("\nÐÅÇÓËÜÒÀÒÛ:")
    print(f"Ïåëüìåííûå àâòîìàòû: {n_pa}")
    print(f"Òåñòîìåñèëüíûå ìàøèíû: {n_tm}")
    print(f"Êóòòåðû: {n_k}")

