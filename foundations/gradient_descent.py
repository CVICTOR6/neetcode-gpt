class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^
        minimizer = init
        # Derivative:         f'(x) = 2x
        for _ in range(iterations):
            derivative = 2 * minimizer
        # Update rule:        x = x - learning_rate * f'(x)
            minimizer = minimizer - learning_rate * derivative
        # Round final answer to 5 decimal places
        return round(minimizer, 5)