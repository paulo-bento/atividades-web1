import logging
import time

logger = logging.getLogger('globaldocs')

class TempoExecucaoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        inicio = time.time()
        response = self.get_response(request)
        fim = time.time()
        duracao = fim - inicio
        logger.info(f"Requisição para {request.path} executada em {duracao:.2f} segundos.")
        return response
