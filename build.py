import re
import os

DIC_FILE = 'DarhanBektaban.dic'
WORDS_FILE = 'words.txt'
INPUT_FILE = 'input.txt'

def load_existing_words():
    """Burynghy zhjnaqtalghan suoizderdi oqyp aluu"""
    existing_words = set()
    
    # 1. DarhanBektaban.dic qojyndydan oquu
    if os.path.exists(DIC_FILE):
        with open(DIC_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            # 1-zholdaghy sandardy (suoiz sanyn) uoitkizip zhiberemiz
            start_idx = 1 if lines and lines[0].strip().isdigit() else 0
            for line in lines[start_idx:]:
                word = line.strip().lower()
                if word:
                    existing_words.add(word)
                    
    # 2. words.txt qojyndy bar bolsa, ony da qosyp aluu
    if os.path.exists(WORDS_FILE):
        with open(WORDS_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                word = line.strip().lower()
                if word:
                    existing_words.add(word)
                    
    return existing_words

def extract_words_from_input():
    """input.txt qojyndydan zhagna maitindi oqyp, suoizderdi buoilip aluu"""
    new_words = set()
    if os.path.exists(INPUT_FILE):
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            text = f.read()
            # Latyn aripterinen turatyn suoizderdi buoilip aluu
            found = re.findall(r'[a-zA-Z]+', text)
            for word in found:
                cleaned = word.strip().lower()
                if len(cleaned) > 0:
                    new_words.add(cleaned)
    return new_words

def build():
    # Burynghy suoizder men zhagna suoizderdi biriktiruu
    existing = load_existing_words()
    new_extracted = extract_words_from_input()
    
    all_words = existing.union(new_extracted)
    
    if not all_words:
        print("Qate: Uoigndejtin suoiz tabylmady!")
        return

    # Ailippe retimen suryptauu
    sorted_words = sorted(list(all_words))
    
    # 1. words.txt qojyndynyn zhagnartyp saqtauu
    with open(WORDS_FILE, 'w', encoding='utf-8') as f:
        for word in sorted_words:
            f.write(f"{word}\n")
            
    # 2. DarhanBektaban.dic qojyndynan Hunspell standartymen zhazuu (1-zholda suoiz sany)
    with open(DIC_FILE, 'w', encoding='utf-8') as f:
        f.write(f"{len(sorted_words)}\n")
        for word in sorted_words:
            f.write(f"{word}\n")

    print("=" * 45)
    print("Zhjnaqtauu saitti ajaqtaldy!")
    print(f"Burynghy suoiz sany: {len(existing)}")
    print(f"Qosylghan zhagna suoizder sany: {len(all_words) - len(existing)}")
    print(f"Zhalpy suoizdik qory (Ailippe retimen): {len(sorted_words)} suoiz")
    print("=" * 45)

if __name__ == '__main__':
    build()
