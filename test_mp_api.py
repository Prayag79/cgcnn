from mp_api.client import MPRester

MP_API_KEY =  '9TJvw6psDp9Kz2P0MCS2pe9s88laGpa9'

def main():
    # connect to Materials Project 
    with MPRester(MP_API_KEY) as mpr:
        # ask for a known material by ID, e.g. silicon mp-149
        doc = mpr.summary.get_data_by_id("mp-149")

    # print some basic info
    print("Material ID:", doc.material_id)
    print("Formula:", doc.formula_pretty)
    print("Formation energy per atom:", doc.formation_energy_per_atom)
    print("Band gap:", doc.band_gap)

if __name__ == "__main__":
    main()

