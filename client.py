import hashlib

class SymmetricRatchet:
    """
    Signal Protocol Symmetric KDF Ratchet Chain.
    Produces unique per-message ephemeral keys and advances internal chain key state.
    """
    def __init__(self, root_key):
        self.chain_key = root_key
        self.step_count = 0

    def step(self):
        msg_key = hashlib.sha256((self.chain_key + ":message").encode()).hexdigest()[:16]
        self.chain_key = hashlib.sha256((self.chain_key + ":advance").encode()).hexdigest()[:16]
        self.step_count += 1
        return msg_key
