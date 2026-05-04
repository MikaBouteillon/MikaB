<?php
/**
 * Footer — pied de page, infos club, réseaux, mentions.
 */
defined( 'ABSPATH' ) || exit;
?>
</main><!-- #main -->

<footer class="bg-usam-charcoal text-usam-bone mt-24">
	<div class="container mx-auto px-4 lg:px-8 py-16 grid gap-12 lg:grid-cols-4">

		<div class="lg:col-span-1">
			<a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="flex items-center gap-3 mb-4">
				<img src="<?php echo esc_url( USAM_THEME_URI . '/assets/images/logo-monogramme.svg' ); ?>"
				     alt="USAM Nîmes Gard" class="h-14 w-14">
				<span class="font-display tracking-widest text-xl">USAM <span class="text-usam-volt">NÎMES</span></span>
			</a>
			<p class="text-sm text-usam-bone/70 leading-relaxed">
				Club professionnel de handball — Liqui Moly Starligue.<br>
				Fondé en 1960. Le Parnasse, 3 333 places.
			</p>
		</div>

		<nav class="lg:col-span-1" aria-label="<?php esc_attr_e( 'Liens rapides', 'usam' ); ?>">
			<h2 class="font-display uppercase tracking-widest text-sm text-usam-volt mb-4">Le club</h2>
			<?php
			wp_nav_menu( [
				'theme_location' => 'footer',
				'container'      => false,
				'menu_class'     => 'space-y-2 text-sm',
				'fallback_cb'    => function () {
					echo '<ul class="space-y-2 text-sm">'
					   . '<li><a href="' . esc_url( home_url( '/le-club/' ) ) . '" class="hover:text-usam-volt">Histoire & palmarès</a></li>'
					   . '<li><a href="' . esc_url( home_url( '/le-parnasse/' ) ) . '" class="hover:text-usam-volt">Le Parnasse</a></li>'
					   . '<li><a href="' . esc_url( home_url( '/partenaires/' ) ) . '" class="hover:text-usam-volt">Partenaires</a></li>'
					   . '<li><a href="' . esc_url( home_url( '/recrutement/' ) ) . '" class="hover:text-usam-volt">Recrutement</a></li>'
					   . '</ul>';
				},
			] );
			?>
		</nav>

		<div class="lg:col-span-1">
			<h2 class="font-display uppercase tracking-widest text-sm text-usam-volt mb-4">Contact</h2>
			<address class="not-italic text-sm space-y-2 text-usam-bone/80">
				<p>Le Parnasse<br>160, Avenue du Languedoc<br>30900 Nîmes</p>
				<p><a href="tel:+33466380947" class="hover:text-usam-volt">04 66 38 09 47</a></p>
				<p><a href="mailto:contact@usam-nimesgard.fr" class="hover:text-usam-volt">contact@usam-nimesgard.fr</a></p>
			</address>
		</div>

		<div class="lg:col-span-1">
			<h2 class="font-display uppercase tracking-widest text-sm text-usam-volt mb-4">Suivre la Green Team</h2>
			<ul class="flex gap-4">
				<li><a href="https://www.facebook.com/USAMNimesGard" aria-label="Facebook" class="hover:text-usam-volt">Facebook</a></li>
				<li><a href="https://www.instagram.com/usam_nimes_gard/" aria-label="Instagram" class="hover:text-usam-volt">Instagram</a></li>
				<li><a href="https://www.linkedin.com/company/usam-nimes-gard" aria-label="LinkedIn" class="hover:text-usam-volt">LinkedIn</a></li>
			</ul>
			<form class="mt-6" action="" method="post">
				<label for="newsletter" class="block text-sm mb-2">Newsletter du club</label>
				<div class="flex">
					<input id="newsletter" type="email" required placeholder="votre@email.fr"
					       class="flex-1 bg-usam-bone/10 border border-usam-bone/20 px-3 py-2 text-sm focus:border-usam-volt outline-none">
					<button class="bg-usam-volt text-usam-charcoal px-4 font-display uppercase text-sm">OK</button>
				</div>
			</form>
		</div>
	</div>

	<div class="border-t border-usam-bone/10">
		<div class="container mx-auto px-4 lg:px-8 py-6 flex flex-col sm:flex-row gap-4 justify-between items-center text-xs text-usam-bone/60">
			<p>© <?php echo esc_html( date( 'Y' ) ); ?> USAM Nîmes Gard. Tous droits réservés.</p>
			<?php
			wp_nav_menu( [
				'theme_location' => 'legal',
				'container'      => false,
				'menu_class'     => 'flex gap-6',
				'fallback_cb'    => function () {
					echo '<ul class="flex gap-6">'
					   . '<li><a href="' . esc_url( home_url( '/mentions-legales/' ) ) . '">Mentions légales</a></li>'
					   . '<li><a href="' . esc_url( home_url( '/politique-de-confidentialite/' ) ) . '">Confidentialité</a></li>'
					   . '<li><a href="' . esc_url( home_url( '/cookies/' ) ) . '">Cookies</a></li>'
					   . '</ul>';
				},
			] );
			?>
		</div>
	</div>
</footer>

<?php wp_footer(); ?>
</body>
</html>
