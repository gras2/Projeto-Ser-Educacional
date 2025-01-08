#from fastapi import APIRouter, Depends, HTTPException
#from app.services.powerbi_service import send_data_to_powerbi

#powerbi_router = APIRouter()

#@powerbi_router.post("/")
#async def push_data_to_powerbi(data: dict):
#    """
#    Envia dados para o Power BI.
#    """
#    try:
#        response = await send_data_to_powerbi(data)
#        return {"success": True, "message": "Dados enviados para o Power BI com sucesso!", "response": response}
#    except Exception as e:
#        raise HTTPException(status_code=500, detail=f"Erro ao enviar dados: {str(e)}")