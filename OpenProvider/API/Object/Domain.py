from .Base import Base

class Domain(Base):
    @property
    def full_domain(self):
        if self.domain.name and self.domain.extension:
            return "{0}.{1}".format(self.domain.name, self.domain.extension)
