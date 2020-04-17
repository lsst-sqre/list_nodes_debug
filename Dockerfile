FROM lsstsqre/sciplat-lab:recommended
COPY list_nodes.py /usr/local/bin/list_nodes
CMD [ "/usr/local/bin/list_nodes" ]
LABEL      description="lister: node_list demo" \
             name="lsstsqre/lister" \
             version="0.0.1"

