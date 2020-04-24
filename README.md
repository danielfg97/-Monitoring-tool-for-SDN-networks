# SDN monitoring tool
Herramienta de monitorización de redes SDN utilizando el Stack de Elastic y el controlador Opendaylight.

En primer lugar se definen en **docker-compose.yml** los contenedores docker del escenario, sus direcciones IP dentro de la red, y los volúmenes que garantizan la persistencia del sistema, entre otros aspectos de configuración.

Las carpetas Logstash, Elasticsearch y Kibana contienen la configuración para poder comunicarse entre sí dentro de los contenedores Docker.
La configuración principal del proyecto se encuentra dentro de la carpeta Logstash. Concretamente en la subcarpeta "pipeline" tenemos el código definido en **logstash.conf** para extraer información del controlador, Opendaylight, y del colector sflow, Sflow-rt.

En la carpeta network se encuentra, en primer lugar, el Dockerfile para contruir la imagen mininet y por lo tanto el contenedor que soportará la red silumada. Por otro lado tenemos la subcarpeta mininet en la cual hemos definido diferentes scripts para ejecutar dentro de los hosts mininet y generar tráfico. Además disponemos de scripts para generar la topología en mininet.

La carpeta Opendaylight contiene el Dockerfile para montar el controlador en un Docker container. Se ha decidido usar la versión carbón.

Finalmente tenemos la carpeta sflow en la que definimos este colector de datagramas sflow e instalamos unas features para la aplicación a la que se puede acceder desde http://localhost:8008/. Sin embargo, en el proyecto utilizamos la REST API y no dicha app como tal.

**Para montar el escenario**, en primer lugar tenemos que ejecutar el script **start.sh**. En él que contemos comandos que permiten el acceso de los contenedores al exterior (a mi me dieron problemas y con ellos se solucionó, con ejecutar una vez sirve). También se ejecuta *host +* para poder abrir las ventanas de los host de mininet con xterm. Este último comando si que será necesario ejectuarlo siempre.

Una vez se tengan instaladas las imágenes de todos los módulos en local, ejecutamos **docker-compose up** para montar el escenario.
A continuación, accedemos al contenedor mininet con **docker exec -ti mininet bash**, a la carpeta mininet y ejecutamos bash *mn_topo.sh* para montar la topología, después ejectuamos un *pingall* para que los hosts se encuentren. Abrimos otra ventana para acceder también al contenedor mininet y ejecutamos el comando *sflow_agents.sh* para definir en los switches el origen de los datagramas sflow que se transmitirán al colector.

Dentro de la mininet CLI abrimos las ventanas con xterm de los host en los que queramos generar tráfico. Por ejemplo, h1,h5 y en ellos ejecutamos sus scripts correspondientes, contenidos en la carpeta mininet.

A continuación, en una ventana aparte ejectuamos el siguiente comando para dar este formato específico a los datagramas sflow:

	curl -H "Content-Type:application/json" -X PUT --data '{"keys":"ipsource,ipdestination,tcpsourceport,tcpdestinationport", "value":"bytes", "log":true}' http://localhost:8008/flow/flowgraph-pair/json

Después accedemos al contenedor logstash y ejectuamos **bin/logstash -f pipeline/logstash.conf --path.data .** para comenzar la extracción de datos. Mientras se recogen datos puede generarse más tráfico en los hosts.

Pueden hacerse búsquedas de los datos en bruto recogidos en Elasticsearch, accesible desde localhost:9200.
Finalmente accedemos a Kibana en localhost:5601 donde podemos visualizar todos los resultados en forma de visualizaciones y dashboards.

Para cerrar el escenario ejecutamos **docker-compose down**.
