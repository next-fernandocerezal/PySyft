# stdlib
import uuid

# relative
from ..tensor import AutogradTensor
from .op import Op


class RShiftOp(Op):
    def forward(self, x: AutogradTensor, y: AutogradTensor) -> AutogradTensor:
        self.x = x
        self.y = y
        # This is just a placeholder to suppress linting errors until the method is built out
        return x

    def _backward(self, grad: AutogradTensor, backprop_id: uuid.UUID) -> None:
        if self.x.requires_grad:
            pass

        if self.y.requires_grad:
            pass
