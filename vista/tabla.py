# Tablas que se muestran en la consola.


def mostrar_no_estable(escenario):
    print(f"\n{escenario.nombre}: λ = {escenario.llegada} no es menor que "
          f"μ = {escenario.servicio}. El sistema no es estable.")


def mostrar_teoria(resultados):
    print("\n=== Valores teóricos ===")
    print(f"{'Escenario':<14}{'λ':>6}{'μ':>6}{'ρ':>9}{'L':>9}{'Lq':>9}{'W':>9}{'Wq':>9}")
    for r in resultados:
        e = r["escenario"]
        t = r["teoria"]
        print(f"{e.nombre:<14}{e.llegada:>6}{e.servicio:>6}{t.rho:>9.3f}"
              f"{t.L:>9.3f}{t.Lq:>9.3f}{t.W:>9.3f}{t.Wq:>9.3f}")


def mostrar_comparacion(resultados):
    print("\n=== Teoría vs simulación ===")
    print(f"{'Escenario':<14}{'Wq teórico':>12}{'Wq simulado':>13}{'Dif %':>8}"
          f"{'Lq teórico':>13}{'Lq simulado':>13}{'Dif %':>8}")
    for r in resultados:
        e = r["escenario"]
        t = r["teoria"]
        dif_espera = (r["espera_simulada"] - t.Wq) / t.Wq * 100
        dif_cola = (r["cola_simulada"] - t.Lq) / t.Lq * 100
        print(f"{e.nombre:<14}{t.Wq:>12.3f}{r['espera_simulada']:>13.3f}{dif_espera:>8.1f}"
              f"{t.Lq:>13.3f}{r['cola_simulada']:>13.3f}{dif_cola:>8.1f}")
