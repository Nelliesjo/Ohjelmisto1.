def delete(kluvut):
    parilliset = []
    for luku in kluvut:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset


def main():
    luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    parilliset = delete(luvut)
    print(f"Alkuperäinen lista: {luvut}")
    print(f"Karsittu lista: {parilliset}")

main()
