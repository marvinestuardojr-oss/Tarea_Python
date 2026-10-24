def sistema_costos_el_nectar():
    print("=========================================================")
    print("   SISTEMA DE COSTOS POR PROCESOS - 'EL NÉCTAR' S.A.     ")
    print("=========================================================\n")

    print("--- FASE 1: DEPARTAMENTO 1 (MEZCLADO) ---")
    costo_mpd1 = float(input("Ingrese Costo de MPD (Q.): "))
    costo_cc1 = float(input("Ingrese Costo de Conversión (Q.): "))
    unid_term1 = float(input("Unidades Terminadas y Transferidas: "))
    unid_proc1 = float(input("Unidades en Proceso: "))
    avance_cc1 = (
        float(input("Porcentaje de avance de conversión (ej. 50): ")) / 100.0
    )

    ue_mpd1 = unid_term1 + unid_proc1
    ue_cc1 = unid_term1 + (unid_proc1 * avance_cc1)

    cu_mpd1 = costo_mpd1 / ue_mpd1
    cu_cc1 = costo_cc1 / ue_cc1
    cu_total1 = cu_mpd1 + cu_cc1

    costo_transferido = unid_term1 * cu_total1
    inv_proceso1 = (unid_proc1 * cu_mpd1) + (unid_proc1 * avance_cc1 * cu_cc1)

    print("\n--- RESUMEN DEPARTAMENTO 1 ---")
    print(f"Unidades Equivalentes MPD: {ue_mpd1:,.0f}")
    print(f"Unidades Equivalentes Conversión: {ue_cc1:,.0f}")
    print(f"Costo Unitario Depto 1: Q. {cu_total1:.2f}")
    print(f"COSTO TRANSFERIDO AL DEPTO 2: Q. {costo_transferido:,.2f}")
    print(f"Inventario en Proceso Depto 1: Q. {inv_proceso1:,.2f}\n")

    print("=========================================================")
    print("--- FASE 2: DEPARTAMENTO 2 (ENVASADO) ---")

    unid_recibidas2 = unid_term1
    costo_recibido2 = costo_transferido

    print(f"[AUTO] Unidades recibidas del Depto 1: {unid_recibidas2:,.0f}")
    print(f"[AUTO] Costo recibido del Depto 1: Q. {costo_recibido2:,.2f}")

    costo_mpd2 = float(input("Ingrese Costo MPD (Botellas) (Q.): "))
    costo_cc2 = float(input("Ingrese Costo de Conversión (Q.): "))
    unid_term2 = float(input("Unidades Terminadas (Listas para venta): "))
    unid_proc2 = float(input("Unidades en Proceso: "))
    avance_cc2 = (
        float(input("Porcentaje de avance de conversión (ej. 40): ")) / 100.0
    )

    ue_mpd2 = unid_term2 + unid_proc2
    ue_cc2 = unid_term2 + (unid_proc2 * avance_cc2)

    cu_transf2 = costo_recibido2 / unid_recibidas2
    cu_mpd2 = costo_mpd2 / ue_mpd2
    cu_cc2 = costo_cc2 / ue_cc2
    cu_propio2 = cu_mpd2 + cu_cc2

    cu_acumulado = cu_transf2 + cu_propio2

    val_producto_terminado = unid_term2 * cu_acumulado
    val_inv_proceso2 = (
        (unid_proc2 * cu_transf2)
        + (unid_proc2 * cu_mpd2)
        + (unid_proc2 * avance_cc2 * cu_cc2)
    )

    print("\n=========================================================")
    print("                REPORTE FINAL DE COSTOS                  ")
    print("=========================================================")
    print(f"Unidades Equivalentes MPD Depto 2: {ue_mpd2:,.0f}")
    print(f"Unidades Equivalentes Conversión Depto 2: {ue_cc2:,.0f}")
    print(f"Costo Unitario Depto 1 (Transferido): Q. {cu_transf2:.2f}")
    print(f"Costo Unitario Propio Depto 2: Q. {cu_propio2:.2f}")
    print(f"COSTO UNITARIO ACUMULADO TOTAL: Q. {cu_acumulado:.2f}")
    print("---------------------------------------------------------")
    print(
        f"VALOR PRODUCTO TERMINADO (VENTA): Q. {val_producto_terminado:,.2f}"
    )
    print(f"VALOR INVENTARIO EN PROCESO FINAL D2: Q. {val_inv_proceso2:,.2f}")
    print("=========================================================")


if __name__ == "__main__":
    sistema_costos_el_nectar()