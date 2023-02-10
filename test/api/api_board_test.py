import allure
from api.BoardApi import BoardApi
import pytest

@pytest.mark.skip
def test_create_board(api_client: BoardApi, delete_board: dict):
    board_list_before = api_client.get_all_boards_by_org_id("617910020c566f69cac8e33d")
    
    resp = api_client.create_board("New board to be deleted")
    delete_board["board_id"] = resp.get("id")
    
    board_list_after = api_client.get_all_boards_by_org_id("617910020c566f69cac8e33d")
    
    with allure.step("Проверить, что количество досок стало больше на 1"):
        assert len(board_list_after) - len(board_list_before) == 1

@pytest.mark.skip
def test_delete_board(api_client: BoardApi, dummy_board_id: str):
    board_list_before = api_client.get_all_boards_by_org_id("617910020c566f69cac8e33d")
    
    api_client.delete_board_by_id(dummy_board_id)
    
    board_list_after = api_client.get_all_boards_by_org_id("617910020c566f69cac8e33d")
    
    with allure.step("Проверить, что количество досок стало меньше на 1"):
        assert len(board_list_before) - len(board_list_after) == 1