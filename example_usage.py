from client import SymmetricRatchet

def main():
    print("=== Testing Signal Symmetric Ratchet ===")
    ratchet = SymmetricRatchet("root_entropy_seed_98765")
    
    k1 = ratchet.step()
    k2 = ratchet.step()
    k3 = ratchet.step()
    
    print(f"Msg Key 1: {k1}")
    print(f"Msg Key 2: {k2}")
    print(f"Msg Key 3: {k3}")
    
    assert len({k1, k2, k3}) == 3, "Ratchet keys must be distinct"
    assert ratchet.step_count == 3
    print("=== Ratchet Verification Complete ===")

if __name__ == "__main__":
    main()
