from .Base import Base
from OpenProvider.API.Object.Domain import Domain as DomainObject

class Domain(Base):
    def search(self, limit=None, offset=None, extension=None,
            domain_name_pattern=None, contact_handle=None, ns_group_pattern=None,
            status=None, with_additional_data=None):
        """Return a list of domain object matching search criteria."""
        request = {
            'searchDomainRequest': {
                'limit': limit,
                'offset': offset,
                'extension': extension,
                'domainNamePattern': domain_name_pattern,
                'contactHandle': contact_handle,
                'nsGroupPattern': ns_group_pattern,
                'status': status,
                'widthAdditionalData': with_additional_data,
            }
        }

        response = self.request(request)
        total = int(response['total'])
        domains = []

        if total == 1:
            domains = [DomainObject(response['results']['array']['item'])]
        elif total > 1:
            domains = [DomainObject(domain) for domain in response['results']['array']['item']]

        return domains

    def retrieve(self):
        """Retrieves information about an existing domain object."""
        pass

    def check(self):
        """Returns the availability of one or more domain names."""
        pass

    def create(self):
        """Registers a domain name with the attributes provided."""
        pass

    def transfer(self):
        """Used to start or schedule domain transfer."""
        pass

    def trade(self):
        """Changes the owner of an existing domain."""
        pass

    def modify(self):
        """Used to modify the attributes of the domain existing in reseller account."""
        pass

    def renew(self):
        """Used to renew domain name in reseller account for specified period."""
        pass

    def delete(self):
        """Deletes a domain name."""
        pass

    def restore(self):
        """Reactivates (or restores) deleted domain."""
        pass

    def retrievePrice(self):
        """	Retrieves domain price that applies for the reseller."""
        pass

    def approveTransfer(self):
        """Approves or rejects a pending outgoing transfer request."""
        pass

    def requestAuthCode(self):
        """Reads the transfer authorization code (or EPP code) from the registry or triggers the registry to send a code to the domain owner (like in case of e.g. .be and .eu)."""
        pass

    def resetAuthCode(self):
        """Generates new authorization code if registry allows it."""
        pass

    def retrieveAdditionalData(self):
        """Retrieve additional data & fields required to register domain in specific TLD."""
        pass

    def retrieveCustomerAdditionalData(self):
        """Retrieve additional data & fields required to register domain in specific TLD."""
        pass

    def tryAgain(self):
        """Tries a failed action like a Transfer or Trade again using the same parameters as last time you've submitted the command."""
        pass
