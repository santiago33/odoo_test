from odoo import models, api, _
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.constrains('email')
    def _check_unique_email(self):
        """Перевіряє, що e-mail унікальний серед всіх партнерів."""
        for partner in self:
            if partner.email:
                # Ігноруємо тих, у кого email порожній
                existing_partner = self.search([
                    ('email', '=', partner.email),
                    ('id', '!=', partner.id)
                ], limit=1)
                if existing_partner:
                    raise ValidationError(
                        _('Email "%s" is already used by another partner.') % partner.email
                    )
