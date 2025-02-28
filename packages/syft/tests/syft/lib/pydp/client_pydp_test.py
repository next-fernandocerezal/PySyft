# third party
import pytest

# syft absolute
import syft as sy

pytest.importorskip("pydp")


# MADHAVA: this needs fixing
@pytest.mark.xfail(
    reason="This was broken when we switched from using a Dictionary obj store to a SQL one which means"
    + "that there's missing serialization functionality. Please address when you can."
)
@pytest.mark.vendor(lib="pydp")
def test_pydp(root_client: sy.VirtualMachineClient) -> None:
    x_ptr = root_client.pydp.algorithms.laplacian.BoundedMean(
        epsilon=1, lower_bound=1, upper_bound=50, dtype="float"
    )

    input_data = [1, 88, 100, 5, 40, 30, 29, 56, 88, 23, 5, 1] * 100
    list_ptr = root_client.python.List(input_data)

    res_ptr = x_ptr.quick_result(list_ptr)
    res = res_ptr.get()

    assert 22 < res < 35


# MADHAVA: this needs fixing
@pytest.mark.xfail(
    reason="This was broken when we switched from using a Dictionary obj store to a SQL one which means"
    + "that there's missing serialization functionality. Please address when you can."
)
@pytest.mark.vendor(lib="pydp")
def test_pydp_functions(root_client: sy.VirtualMachineClient) -> None:
    x_ptr = root_client.pydp.algorithms.laplacian.BoundedMean(
        epsilon=1, lower_bound=1, upper_bound=50, dtype="float"
    )

    input_data = [1, 88, 100, 5, 40, 30, 29, 56, 88, 23, 5, 1] * 100
    list_ptr = root_client.python.List(input_data)
    x_ptr.add_entries(list_ptr)
    res_ptr = x_ptr.result(0.7)
    assert isinstance(res_ptr.get(), float)

    assert round(x_ptr.privacy_budget_left().get(), 2) == 0.3
