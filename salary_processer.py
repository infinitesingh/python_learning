import services.data_services

from config import logging
def start_processing(content):

    # If you want to save data then transform it and save it

    # Proceed with processing with layered architecture

    if content.get('data').get("ping") == 'ping':
        return {"data":{"ping":"pong"}}
    else:
        # Process here
        logging.info("Starting Salary Processing for contetn: {0}".format( content))
        salary = services.data_services.city_sal_mapping(content.get('data'))
        return {"data":{"ping":"Ping Again", "salary":salary}}
        

