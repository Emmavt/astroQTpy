import numpy as np

from .quadnode import QuadNode
from .quadpoint import QuadPoint
from .basetree import BaseTree


class RandomQuadTree(BaseTree):
    """_summary_

    _extended_summary_

    Args:
        x_min (float): _description_
        x_max (float): _description_
        y_min (float): _description_
        y_max (float): _description_
        split_threshold (float): _description_
        N_points (int, optional): _description_. Defaults to 20.
        min_depth (int, optional): _description_. Defaults to 3.
        max_depth (int, optional): _description_. Defaults to 6.
        N_proc (int, optional): _description_. Defaults to 4.
        verbose (bool, optional): _description_. Defaults to True.
        filename_points (str, optional): _description_. Defaults to 'points.txt'.
        filename_nodes (str, optional): _description_. Defaults to 'nodes.txt'.
    """
    
    def __init__(self,
            x_min: float,
            x_max: float,
            y_min: float,
            y_max: float,
            split_threshold: float,
            N_points: int = 20,
            min_depth: int = 3,
            max_depth: int = 6,
            N_proc: int = 4,
            verbose: bool = True,
            filename_points: str = 'points.txt',
            filename_nodes: str = 'nodes.txt'
            ) -> None:
        """Initialization
        
        Create a random quadtree.
        """
        super().__init__(
            x_min, x_max, y_min, y_max, split_threshold,
            N_points, min_depth, max_depth, N_proc, verbose,
            filename_points, filename_nodes
            )
        
        
    def evaluate_point(self, node: QuadNode, rng_seed: int = 123456):
        """_summary_

        _extended_summary_

        Args:
            node (QuadNode): _description_
            rng_seed (int, optional): _description_. Defaults to 123456.

        Returns:
            _type_: _description_
        """
        
        rng = np.random.default_rng(rng_seed)
        
        point = QuadPoint(
            rng.uniform(node.x_min, node.x_max),
            rng.uniform(node.y_min, node.y_max),
            rng.choice([1, 0])
            )
    
        if self.N_proc > 1:
            return point
            
        else:
            node.node_points.append(point)
    