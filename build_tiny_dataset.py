from mp_api.client import MPRester
import os
import csv

key_path = os.path.join(BASE_DIR, "apikey.txt")
with open(key_path, "r") as f:
    API_KEY = f.read().strip()


# Small test set of MP IDs to build a tiny dataset
TEST_IDS = ["mp-149", "mp-13", "mp-30", "mp-81", "mp-66"]

# Base directory = folder where THIS script lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Data directory where we will save CIFs + id_prop.csv
DATA_DIR = os.path.join(BASE_DIR, "data", "mp_tiny")


def main():
    print("Base directory:", BASE_DIR)
    print("Data directory will be:", DATA_DIR)

    # Make data/mp_tiny if it doesn't exist
    os.makedirs(DATA_DIR, exist_ok=True)

    rows = []

    # Open a connection to Materials Project
    with MPRester(API_KEY) as mpr:
        for mid in TEST_IDS:
            print(f"\nFetching {mid}...")

            # Use the new search API (non-deprecated)
            docs = mpr.materials.summary.search(material_ids=[mid])

            if not docs:
                print(f"  WARNING: no document returned for {mid}, skipping.")
                continue

            doc = docs[0]

            # Save structure as CIF
            cif_path = os.path.join(DATA_DIR, f"{mid}.cif")
            print(f"  Writing CIF to: {cif_path}")
            doc.structure.to(fmt="cif", filename=cif_path)

            # Store (id, formation_energy_per_atom)
            fe = doc.formation_energy_per_atom
            print(f"  formation_energy_per_atom = {fe}")
            rows.append([mid, fe])

    # Write id_prop.csv (no header, just id, property)
    csv_path = os.path.join(DATA_DIR, "id_prop.csv")
    print(f"\nWriting id_prop.csv to: {csv_path}")
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)

    print(" Tiny dataset created under:", DATA_DIR)
    print("Files now in mp_tiny:")
    for name in os.listdir(DATA_DIR):
        print("  -", name)


if __name__ == "__main__":
    main()
