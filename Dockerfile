FROM odoo:19

USER root
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh && chown odoo:odoo /entrypoint.sh

USER odoo
ENTRYPOINT ["/entrypoint.sh"]
