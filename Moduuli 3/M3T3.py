sukupuoli = input("Onko biologinen sukupuolesi nainen vai mies?:")
hgarvo = float(input("Mikä on sinun hemoglobiini arvosi?:"))

if sukupuoli == 'nainen':
    if 117 <= hgarvo < 175:
        print("Hemoglobiiniarvo on normaali.")
    elif 117 > hgarvo:
        print("Hemoglobiini rvo on alhainen.")
    else:
        print("Hemoglobiiniarvo on korkea.")

if sukupuoli == 'mies':
    if 134 <= hgarvo < 195:
        print("hemoglobiiniarvo on normaali.")
    elif 143 > hgarvo:
        print("Hemoglobiini rvo on alhainen.")
    else:
        print("Hemoglobiiniarvo on korkea.")