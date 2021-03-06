..
    Warning: Do not edit this file. It is automatically generated from the
    software project's code and your changes will be overwritten.

    The tool to generate this file lives in openstack-doc-tools repository.

    Please make any changes needed in the code, then run the
    autogenerate-config-doc tool from the openstack-doc-tools repository, or
    ask for help on the documentation mailing list, IRC channel or meeting.

.. _ec2api-ec2:

.. list-table:: Description of EC2API configuration options
   :header-rows: 1
   :class: config-ref-table

   * - Configuration option = Default value
     - Description

   * - **[DEFAULT]**
     -

   * - ``default_flavor`` = ``m1.small``

     - (String) A flavor to use as a default instance type

   * - ``disable_ec2_classic`` = ``None``

     - (Boolean) True if server does not support EC2 Classic mode in favor of default VPC

   * - ``ec2_host`` = ``$my_ip``

     - (String) The IP address of the EC2 API server

   * - ``ec2_path`` = ``/``

     - (String) The path prefix used to call the ec2 API server

   * - ``ec2_port`` = ``8788``

     - (Integer) The port of the EC2 API server

   * - ``ec2_private_dns_show_ip`` = ``False``

     - (Boolean) Return the IP address as private dns hostname in describe instances

   * - ``ec2_scheme`` = ``http``

     - (String) The protocol to use when connecting to the EC2 API server (http, https)

   * - ``external_network`` = ``None``

     - (String) Name of the external network, which is used to connectVPCs to Internet and to allocate Elastic IPs.

   * - ``internal_service_availability_zone`` = ``internal``

     - (String) The availability_zone to show internal services under

   * - ``my_ip`` = ``10.0.0.1``

     - (String) IP address of this host

   * - ``network_device_mtu`` = ``1500``

     - (Integer) MTU size to set by DHCP for instances. Corresponds with the network_device_mtu in ec2api.conf.

   * - ``region_list`` =

     - (List) List of region=fqdn pairs separated by commas
