from .Base import Base

class Domain(Base):
    @property
    def full_domain(self):
        """Get the full domain including the name and extension"""
        if hasattr(self, 'domain'):
            if isinstance(self.domain, str):
                return self.domain
            if hasattr(self.domain, 'name') and hasattr(self.domain, 'extension'):
                return "{0}.{1}".format(self.domain.name, self.domain.extension)
