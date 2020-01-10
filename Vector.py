from typing import List
import math

Vector = List[float]


def add(v: Vector, w: Vector) -> Vector:
    """Adds Corresponding Elements"""
    assert len(v) == len(w)
    return [v_i + w_i for v_i, w_i in zip(v, w)]


print(add([1, 2, 3], [4, 5, 6]))


def subtract(v: Vector, w: Vector) -> Vector:
    """Subtract the corresponding Elements"""
    assert len(v) == len(w)
    return [v_i - w_i for v_i, w_i in zip(v, w)]


print(subtract([5, 7, 9], [4, 5, 6]))


def vector_sum(vectors: List[float]) -> Vector:
    """Sum All corresponding Elements"""
    assert vectors, "No elements provided"

    # Check whether all elements are of same size or not
    num_elements = len(vectors[0])
    assert all(
        len(v) == num_elements for v in vectors), "Elements are of different sizes"

    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]


print(vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]))


def scalar_multiply(c: float, vector: Vector) -> Vector:
    "Multiplies a constant c with vector"
    return [c * v_i for v_i in vector]


def vector_mean(vector: Vector) -> Vector:
    """Computes the element-wise average"""
    num_len = len(vector)
    return scalar_multiply(1/num_len, vector_sum(vector))


print(vector_mean([[1, 2], [3, 4], [5, 6]]))


def dot(v: Vector, w: Vector) -> float:
    assert len(v) == len(w)
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v: Vector) -> float:
    return dot(v, v)


def magnitude(v: Vector) -> float:
    """Returns the magnitude or length of v"""
    return math.sqrt(sum_of_squares(v))


def squared_distance(v: Vector, w: Vector) -> float:
    return sum_of_squares(v, w)

def distance(v:Vector,w:Vector)->float:
  return math.sqrt(squared_distance(v,w))


