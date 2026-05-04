<?php
/**
 * Page d'accueil — hero, prochain match, dernières news, équipes, partenaires.
 */
defined( 'ABSPATH' ) || exit;

get_header(); ?>

<!-- HERO -->
<section class="relative bg-usam-charcoal text-usam-bone overflow-hidden">
	<div class="absolute inset-0 opacity-30 bg-[radial-gradient(circle_at_30%_20%,rgba(0,230,118,0.4),transparent_60%)]"></div>
	<div class="container mx-auto px-4 lg:px-8 py-24 lg:py-32 relative">
		<p class="font-display uppercase tracking-[0.4em] text-usam-volt text-sm mb-6">Liqui Moly Starligue · Saison 2025/26</p>
		<h1 class="font-display uppercase text-6xl md:text-8xl lg:text-9xl leading-[0.9] mb-8">
			La <span class="text-usam-volt">Green</span><br>Team
		</h1>
		<p class="text-lg md:text-xl max-w-xl text-usam-bone/80 mb-10">
			Depuis 1960 à Nîmes, l'USAM porte les couleurs du Gard au plus haut niveau du handball français. Bienvenue au Parnasse.
		</p>
		<div class="flex flex-wrap gap-4">
			<?php usam_cta( 'Billetterie', 'https://billetterie.usam-nimesgard.fr', 'primary' ); ?>
			<?php usam_cta( 'Le calendrier', home_url( '/calendrier/' ), 'secondary' ); ?>
		</div>
	</div>
</section>

<!-- PROCHAIN MATCH -->
<?php $next = usam_get_next_match( 'green-team' ); if ( $next ) : ?>
<section class="bg-usam-volt text-usam-charcoal">
	<div class="container mx-auto px-4 lg:px-8 py-8 flex flex-wrap items-center justify-between gap-6">
		<div>
			<p class="font-display uppercase tracking-widest text-xs">Prochain match</p>
			<h2 class="font-display uppercase text-3xl md:text-4xl">
				USAM <span class="opacity-50">vs</span> <?php echo esc_html( get_post_meta( $next->ID, 'usam_match_adversaire', true ) ); ?>
			</h2>
			<p class="text-sm">
				<?php echo esc_html( wp_date( 'l j F · H\hi', strtotime( get_post_meta( $next->ID, 'usam_match_date', true ) ) ) ); ?>
				· <?php echo esc_html( get_post_meta( $next->ID, 'usam_match_lieu', true ) ); ?>
			</p>
		</div>
		<?php
		$billet = get_post_meta( $next->ID, 'usam_match_billetterie_url', true );
		if ( $billet ) {
			usam_cta( 'Réserver ma place', $billet, 'primary' );
		}
		?>
	</div>
</section>
<?php endif; ?>

<!-- LES ÉQUIPES -->
<section class="container mx-auto px-4 lg:px-8 py-20">
	<header class="mb-12 max-w-2xl">
		<p class="font-display uppercase tracking-widest text-usam-volt text-sm mb-2">Les équipes</p>
		<h2 class="font-display uppercase text-4xl md:text-5xl">Un club, plusieurs combats</h2>
	</header>

	<div class="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
		<?php
		$equipes = [
			[ 'green-team', 'Green Team', 'Liqui Moly Starligue', 'pro-masculine' ],
			[ 'nimoises', 'Les Nîmoises', 'D2 Féminine', 'pro-feminine' ],
			[ 'n1m', 'Réserve N1M', 'Nationale 1 Masculine', 'reserve' ],
			[ 'n3f', 'Réserve N3F', 'Nationale 3 Féminine', 'n3f' ],
			[ 'formation', 'Centre de formation', 'Académie Espoirs', 'formation' ],
			[ 'ecole', 'École de hand', 'Jeunes & loisir', 'ecole-de-hand' ],
		];
		foreach ( $equipes as [ $slug, $titre, $sous, $page ] ) : ?>
			<a href="<?php echo esc_url( home_url( '/equipes/' . $page . '/' ) ); ?>"
			   class="group bg-usam-charcoal text-usam-bone p-8 border-l-4 border-usam-volt hover:bg-usam-forest transition">
				<p class="font-display uppercase tracking-widest text-xs text-usam-volt mb-2"><?php echo esc_html( $sous ); ?></p>
				<h3 class="font-display uppercase text-2xl group-hover:translate-x-1 transition"><?php echo esc_html( $titre ); ?></h3>
			</a>
		<?php endforeach; ?>
	</div>
</section>

<!-- DERNIÈRES ACTUS -->
<section class="bg-usam-bone py-20">
	<div class="container mx-auto px-4 lg:px-8">
		<header class="mb-12 flex justify-between items-end">
			<div>
				<p class="font-display uppercase tracking-widest text-usam-volt text-sm mb-2">Le fil</p>
				<h2 class="font-display uppercase text-4xl md:text-5xl">Dernières actus</h2>
			</div>
			<?php usam_cta( 'Toutes les actus', home_url( '/actus/' ), 'ghost' ); ?>
		</header>

		<?php
		$actus = new WP_Query( [ 'post_type' => 'post', 'posts_per_page' => 3 ] );
		if ( $actus->have_posts() ) : ?>
			<div class="grid gap-8 md:grid-cols-3">
			<?php while ( $actus->have_posts() ) : $actus->the_post(); ?>
				<article class="bg-white border border-usam-slate-200 group">
					<?php if ( has_post_thumbnail() ) : ?>
						<a href="<?php the_permalink(); ?>" class="block aspect-video overflow-hidden">
							<?php the_post_thumbnail( 'usam-card', [ 'class' => 'w-full h-full object-cover group-hover:scale-105 transition' ] ); ?>
						</a>
					<?php endif; ?>
					<div class="p-6">
						<p class="text-xs uppercase tracking-widest text-usam-slate-700 mb-2"><?php echo esc_html( get_the_date( 'j F Y' ) ); ?></p>
						<h3 class="font-display uppercase text-xl mb-3">
							<a href="<?php the_permalink(); ?>" class="hover:text-usam-volt"><?php the_title(); ?></a>
						</h3>
						<p class="text-sm text-usam-slate-700"><?php echo esc_html( wp_trim_words( get_the_excerpt(), 18 ) ); ?></p>
					</div>
				</article>
			<?php endwhile; wp_reset_postdata(); ?>
			</div>
		<?php else : ?>
			<p class="text-usam-slate-700">Pas d'actus publiées pour l'instant.</p>
		<?php endif; ?>
	</div>
</section>

<!-- LE PARNASSE -->
<section class="bg-usam-charcoal text-usam-bone py-20">
	<div class="container mx-auto px-4 lg:px-8 grid gap-12 lg:grid-cols-2 items-center">
		<div>
			<p class="font-display uppercase tracking-widest text-usam-volt text-sm mb-2">Notre maison</p>
			<h2 class="font-display uppercase text-4xl md:text-5xl mb-6">Le Parnasse</h2>
			<p class="text-usam-bone/80 mb-6 leading-relaxed">
				3 333 places. Un chaudron debout, des soirs de Starligue qui font trembler les vitres.
				Vingt fois par saison, on y défend nos couleurs devant le meilleur public du Sud.
			</p>
			<?php usam_cta( "Visiter Le Parnasse", home_url( '/le-parnasse/' ), 'secondary' ); ?>
		</div>
		<div class="aspect-video bg-usam-forest border border-usam-volt/30 flex items-center justify-center text-usam-volt font-display uppercase tracking-widest">
			[ photo Le Parnasse ]
		</div>
	</div>
</section>

<!-- PARTENAIRES -->
<section class="container mx-auto px-4 lg:px-8 py-20">
	<header class="mb-12 max-w-2xl">
		<p class="font-display uppercase tracking-widest text-usam-volt text-sm mb-2">Ils nous soutiennent</p>
		<h2 class="font-display uppercase text-4xl md:text-5xl">Partenaires</h2>
	</header>

	<div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-px bg-usam-slate-200">
		<?php
		$logos = new WP_Query( [
			'post_type'      => 'partenaire',
			'posts_per_page' => 15,
		] );
		if ( $logos->have_posts() ) : while ( $logos->have_posts() ) : $logos->the_post(); ?>
			<a href="<?php echo esc_url( get_post_meta( get_the_ID(), 'usam_partenaire_url', true ) ?: '#' ); ?>"
			   class="aspect-[3/2] bg-white flex items-center justify-center p-6 hover:bg-usam-bone transition">
				<?php if ( has_post_thumbnail() ) : the_post_thumbnail( 'usam-thumb-square', [ 'class' => 'max-h-full max-w-full object-contain' ] );
				else : echo '<span class="text-sm text-usam-slate-700">' . esc_html( get_the_title() ) . '</span>';
				endif; ?>
			</a>
		<?php endwhile; wp_reset_postdata();
		else: ?>
			<p class="col-span-full p-8 bg-white text-usam-slate-700">Liste des partenaires à venir.</p>
		<?php endif; ?>
	</div>

	<p class="mt-8 text-center">
		<a href="<?php echo esc_url( home_url( '/devenir-partenaire/' ) ); ?>" class="text-usam-volt underline-offset-4 hover:underline font-display uppercase tracking-widest text-sm">
			Devenir partenaire →
		</a>
	</p>
</section>

<?php get_footer();
