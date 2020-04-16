FROM sflow/sflow-rt:latest

MAINTAINER Daniel Fernandez Gordo

ENV RTAPP="-Dhttp.html.redirect=./app/top-flows/html/"
RUN /sflow-rt/get-app.sh sflow-rt top-flows
RUN /sflow-rt/get-app.sh sflow-rt flow-trend
RUN /sflow-rt/get-app.sh sflow-rt browse-metrics
RUN /sflow-rt/get-app.sh sflow-rt flow-graph
RUN /sflow-rt/get-app.sh sflow-rt trace-flow
