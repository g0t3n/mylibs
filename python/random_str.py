def random_string(length):
    import M2Crypto.Rand
    return M2Crypto.Rand.rand_bytes(length)

