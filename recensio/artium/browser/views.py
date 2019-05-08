from recensio.theme.browser.homepage import HomepageView
from recensio.theme.browser.pdfgen import GeneratePdfRecension


class GeneratePdfRecensionArtium(GeneratePdfRecension):
    """Customized cover page
    """
    logo_main = '++resource++recensio.artium.images/logo2_fuer-Deckblatt.jpg'


class ArtiumHomepageView(HomepageView):

    review_languages = [u'']
