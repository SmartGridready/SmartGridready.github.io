.. _openapi-specifications:

|dev| OpenAPI Specifications
====================================================

SmartGridready provides OpenAPI specifications for specific use cases:

* :ref:`dynamic_tariffs`

.. _dynamic_tariffs:

Dynamic Tariffs
---------------

The :term:`VSE` has published a `document <https://www.strom.ch/de/shop/dynamische-netznutzungstarife-im-verteilnetz-hdn-ch-2025>`_ which describes the requirements of APIs that deliver dynamic tariff data.

SmartGridready provides OpenAPI specification templates that help developers create a :term:`VSE`-compliant API.

* Display the current OpenAPI specification for dynamic tariffs in `Swagger UI <../_static/swagger/dynamic-tariff.html>`_
* Download the specification and JSON schema on `Github <https://github.com/SmartGridready/SGrSpecifications/tree/openapi-for-dynamic-tariff/DynamicTariff>`_

.. raw:: html

    <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@5.11.0/swagger-ui.css" />
    <div id="swagger-ui-dynamic-tariff"></div>
    <script src="https://unpkg.com/swagger-ui-dist@5.11.0/swagger-ui-bundle.js" crossorigin></script>
    <script>
      window.onload = () => {
        window.ui = SwaggerUIBundle({
          url: 'https://raw.githubusercontent.com/SmartGridready/SGrSpecifications/refs/heads/openapi-for-dynamic-tariff/DynamicTariff/OpenAPI/dynamic_tariff_vse_2026_openapi.yaml',
          dom_id: '#swagger-ui-dynamic-tariff',
        });
      };
    </script>
