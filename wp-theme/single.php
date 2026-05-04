<?php
/**
 * Article (actualité).
 */
defined( 'ABSPATH' ) || exit;

get_header(); ?>

<article class="container mx-auto px-4 lg:px-8 py-16 max-w-3xl">
	<?php while ( have_posts() ) : the_post(); ?>
		<header class="mb-10">
			<p class="text-sm uppercase tracking-widest text-usam-slate-700 mb-3">
				<?php echo esc_html( get_the_date( 'j F Y' ) ); ?>
				· <?php the_category( ', ' ); ?>
			</p>
			<h1 class="font-display uppercase text-4xl md:text-6xl"><?php the_title(); ?></h1>
		</header>

		<?php if ( has_post_thumbnail() ) : ?>
			<figure class="mb-10 -mx-4 lg:-mx-0">
				<?php the_post_thumbnail( 'usam-hero', [ 'class' => 'w-full' ] ); ?>
			</figure>
		<?php endif; ?>

		<div class="prose prose-lg max-w-none prose-headings:font-display prose-headings:uppercase prose-a:text-usam-volt">
			<?php the_content(); ?>
		</div>
	<?php endwhile; ?>
</article>

<?php get_footer();
