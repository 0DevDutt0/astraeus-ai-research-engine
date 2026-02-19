from app.llm.model_router import route_model


def get_llm(role=None):
    return route_model(role)
