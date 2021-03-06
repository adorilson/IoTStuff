import logging
import asyncio
from aiocoap import *
import json
logging.basicConfig(level=logging.INFO)

class CoAPConnection:
    '''
    Classe para recuperar dados de um sensor que utilize CoAP.

    Attributes:
            host (str): Sensor Hostname
            resource(srt): remote CoAP resource
    '''

    def getResource(self, **kwargs):
        return self.getCoAPFloat(kwargs)

    async def getRawCoAP(self, **kwargs):
        protocol = await Context.create_client_context()
        request = Message(code=GET,
                    uri=f'coap://{kwargs["host"]}/kwargs["resource"]'
        try:
            response = await protocol.request(request).response
        except Exception as e:
            print('Failed to fetch resource:')
            print(e)
        else:
            return float(response.payload)

    def getCoAPFloat(self, **kwargs):
        return float(asyncio.get_event_loop().run_until_complete(self.getRawCoAP(kwargs)))
