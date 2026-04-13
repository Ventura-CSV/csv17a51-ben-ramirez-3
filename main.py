from __future__ import annotations


def get_domain(mapping: dict) -> set:
    """Return the domain X (all inputs of the function)."""
    # === TODO ===
    # I put the keys of the mapping into a set to get the unique inputs, which is the domain.
    return set(mapping.keys())
    # === END TODO ===


def get_range(mapping: dict) -> set:
    """Return the range — the set of outputs actually mapped to."""
    # === TODO ===
    # I put the values of the mapping into a set to get the unique outputs, which is the range.
    return set(mapping.values())
    # === END TODO ===


def is_well_defined(mapping: dict, target: set) -> bool:
    """Return True if every output value is in the target set."""
    # === TODO ===
    # I check if the set of values in the mapping is a subset of the target set.
    return set(mapping.values()) <= target
    # === END TODO ===


def is_injective(mapping: dict) -> bool:
    """Return True if f is one-to-one (no two inputs map to same output)."""
    # === TODO ===
    # I check if the number of unique output values is the same as the number of input values.
    return len(set(mapping.values())) == len(mapping)
    # === END TODO ===


def is_surjective(mapping: dict, target: set) -> bool:
    """Return True if f is onto (range == target)."""
    # === TODO ===
    # I check if the set of values in the mapping is equal to the target set.
    return set(mapping.values()) == target
    # === END TODO ===


def is_bijective(mapping: dict, target: set) -> bool:
    """Return True if f is both injective and surjective."""
    # === TODO ===
    # I check if the mapping is both injective and surjective by calling the respective functions.
    return is_injective(mapping) and is_surjective(mapping, target)
    # === END TODO ===
