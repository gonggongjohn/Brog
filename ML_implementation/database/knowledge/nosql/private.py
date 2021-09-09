from py2neo import Graph, Node, Relationship, ogm
from py2neo.matching import RelationshipMatcher

graph = Graph(
    "http://localhost:7474",  # 连接本地端口
    name='neo4j',  # 数据库名称
    auth=("neo4j", "root")  # 登录用户名密码
)

tx = graph.begin()


def init_index(graph: Graph, label_index_list):
    for label, indices in label_index_list:
        _indices = set(graph.schema.get_indexes(label))
        create = indices - _indices
        drop = _indices - indices
        print("为标签: ", label)
        print("添加了索引 ", create, "; 删除了索引 ", drop)
        if create != set():
            graph.schema.create_index(label, *create)
        if drop != set():
            graph.schema.drop_index(label, *drop)


init_index(
    graph=graph,
    label_index_list=[
        ("book", {("book_id", )})
    ]
)

graph.commit(tx)


def drag(node: Node, direction, weight=1, γ=0.5, bound=1/8):
    # 因为weight总是单调递减, 只要不把bound设置到0就不用担心死循环
    if weight < bound:
        return 0
    node["vector"] = γ * weight * direction + (1 - γ) * node["vector"]
    require = list(
        RelationshipMatcher(graph).match((node, None), r_type="require"))
    graph.commit(tx)
    for prerequsite in require:
        drag(prerequsite.end_node,
             prerequsite["weight"] * direction,
             weight=γ * weight,
             bound=bound)
