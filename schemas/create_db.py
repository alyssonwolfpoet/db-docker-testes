from database import Base,engine
from ..models.models import API_KEY

print("Crieating database ...")
Base.metadata.create_all(engine)