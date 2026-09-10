from client import SymmetricRatchet
import json

def handle_request(req):
    root = req.get("root_key", "seed")
    ratchet = SymmetricRatchet(root)
    action = req.get("action")
    if action == "step":
        k = ratchet.step()
        return {"status": "ok", "message_key": k, "next_chain": ratchet.chain_key}
    return {"status": "error", "message": "Unknown action"}

if __name__ == "__main__":
    print(json.dumps(handle_request({"action": "step", "root_key": "test"})))
