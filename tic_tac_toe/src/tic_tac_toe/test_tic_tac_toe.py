import pytest
from tic_tac_toe.tic_tac_toe import main

# Define test cases for the main game loop
@pytest.mark.parametrize("input_values, expected_output", [
    (['1 1', '1 2', '2 1', '2 2', '3 1'], [
        "Welcome to Tic-Tac-Toe!",
        " | | ",
        "-----",
        " | | ",
        "-----",
        " | | ",
        "Player X's turn",
        "Player O's turn",
        "Player X's turn",
        "Player O's turn",
        "Player X's turn",
        "Player X wins!",
    ]),
    (['1 1', '2 1', '1 2', '2 2', '2 3', '1 3', '3 1', '3 2', '3 3'], [
        "Welcome to Tic-Tac-Toe!",
        " | | ",
        "-----",
        " | | ",
        "-----",
        " | | ",
        "Player X's turn",
        "Player O's turn",
        "Player X's turn",
        "Player O's turn",
        "Player X's turn",
        "Player O's turn",
        "Player X's turn",
        "Player O's turn",
        "Player X's turn",
        "Player X's turn",
        "It's a tie!",
    ]),
    (['1 1', '1 2', '2 2', '2 2', '2 3', '3 1', '3 2', '3 3'], [
        "Welcome to Tic-Tac-Toe!",
        " | | ",
        "-----",
        " | | ",
        "-----",
        " | | ",
        "Player X's turn",
        "Player O's turn",
        "Player X's turn",
        "Invalid move. Try again.",
        "Player O's turn",
        "Player X's turn",
        "Player O's turn",
        "Player X's turn",
        "Player X's turn",
    ]),
])
def test_main_game(input_values, expected_output, capfd, monkeypatch):
    """
    Test the main game loop with different sets of input values and expected output.

    This function runs multiple test cases to simulate games, providing input
    values as if entered by players and checking if the game behaves as expected.

    Args:
        input_values (list): List of strings representing player input.
        expected_output (list): List of strings representing the expected output.
        capfd (pytest.fixture): Capturing the standard output.
        monkeypatch (pytest.fixture): Mocking the input function for testing.

    Returns:
        None
    """
    with pytest.raises(SystemExit):
        monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
        main()

    out, _ = capfd.readouterr()
    output_lines = out.strip().split('\n')

    # Check if the actual output matches the expected output
    assert output_lines == expected_output
