from pydantic import BaseModel,Field
from typing import Literal


class SkinPredictionResponse(BaseModel):
    skin_condition: Literal['Boil','clear skin',
                            'Eczema','keloids',
                            'Vitiligo'] = Field(...,description='The predicted skin condition based on the input image',
                                                examples=['Vitiligo'])
    probability: float = Field(..., ge=0.0, le=1.0,
                               description='The probability associated with the predicted class of skin condition',
                               examples=[0.567])
