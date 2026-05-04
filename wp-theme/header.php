<?php
/**
 * Header — en-tête HTML, nav, bandeau alerte match.
 */
defined( 'ABSPATH' ) || exit;
?>
<!doctype html>
<html <?php language_attributes(); ?> class="scroll-smooth">
<head>
	<meta charset="<?php bloginfo( 'charset' ); ?>">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="theme-color" content="#0A0A0A">
	<link rel="profile" href="https://gmpg.org/xfn/11">
	<?php wp_head(); ?>
</head>
<body <?php body_class( 'bg-usam-bone text-usam-charcoal antialiased' ); ?>>
<?php wp_body_open(); ?>

<a class="sr-only focus:not-sr-only focus:absolute focus:top-2 focus:left-2 bg-usam-volt text-usam-charcoal px-3 py-2" href="#main">
	<?php esc_html_e( 'Aller au contenu', 'usam' ); ?>
</a>

<header id="masthead" class="bg-usam-charcoal text-usam-bone sticky top-0 z-50 border-b border-usam-volt/20">
	<div class="container mx-auto flex items-center justify-between py-4 px-4 lg:px-8">

		<a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="flex items-center gap-3" aria-label="USAM Nîmes Gard, retour à l'accueil">
			<?php if ( has_custom_logo() ) : ?>
				<?php the_custom_logo(); ?>
			<?php else : ?>
				<img src="<?php echo esc_url( USAM_THEME_URI . '/assets/images/logo-monogramme.svg' ); ?>"
				     alt="USAM Nîmes Gard" class="h-12 w-12">
				<span class="font-display tracking-widest text-xl">USAM <span class="text-usam-volt">NÎMES</span></span>
			<?php endif; ?>
		</a>

		<nav aria-label="<?php esc_attr_e( 'Navigation principale', 'usam' ); ?>" class="hidden lg:block">
			<?php
			wp_nav_menu( [
				'theme_location' => 'primary',
				'container'      => false,
				'menu_class'     => 'flex items-center gap-8 font-display uppercase text-sm tracking-wide',
				'fallback_cb'    => function () {
					echo '<ul class="flex items-center gap-8 font-display uppercase text-sm tracking-wide">'
					   . '<li><a href="' . esc_url( home_url( '/le-club/' ) ) . '">Le Club</a></li>'
					   . '<li><a href="' . esc_url( home_url( '/equipes/' ) ) . '">Équipes</a></li>'
					   . '<li><a href="' . esc_url( home_url( '/ecole-de-hand/' ) ) . '">École de hand</a></li>'
					   . '<li><a href="' . esc_url( home_url( '/actus/' ) ) . '">Actus</a></li>'
					   . '<li><a href="' . esc_url( home_url( '/partenaires/' ) ) . '">Partenaires</a></li>'
					   . '<li><a href="' . esc_url( home_url( '/contact/' ) ) . '">Contact</a></li>'
					   . '</ul>';
				},
			] );
			?>
		</nav>

		<div class="flex items-center gap-3">
			<a href="https://billetterie.usam-nimesgard.fr"
			   class="hidden sm:inline-flex items-center px-4 py-2 bg-usam-yellow text-usam-charcoal font-display uppercase text-sm tracking-wide hover:bg-usam-volt transition">
				Billetterie
			</a>
			<button type="button"
			        class="lg:hidden p-2 text-usam-bone"
			        aria-label="<?php esc_attr_e( 'Ouvrir le menu', 'usam' ); ?>"
			        data-usam-mobile-toggle>
				<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor"
				     stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
					<line x1="3" y1="6" x2="21" y2="6"/>
					<line x1="3" y1="12" x2="21" y2="12"/>
					<line x1="3" y1="18" x2="21" y2="18"/>
				</svg>
			</button>
		</div>
	</div>
</header>

<main id="main" class="min-h-screen">
