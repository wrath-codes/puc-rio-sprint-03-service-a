from flask_cors import CORS
from flask_openapi3 import Info, OpenAPI, Tag

info = Info(
    title="Child Profile API",
    version="1.0.0",
    description="API for Managing Child Profiles",
)

app = OpenAPI(__name__, info=info)
CORS(app)


home_tag = Tag(
    name="Documentation",
    description="Documentation Selection: Swagger, ReDoc or RapiDoc",
)
children_tag = Tag(name="Children", description="Children Profile Management")
