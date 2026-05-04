<?php
/**
 * Page WordPress générique.
 */
defined( 'ABSPATH' ) || exit;

get_header(); ?>

<article class="container mx-auto px-4 lg:px-8 py-16 max-w-3xl">
	<?php while ( have_posts() ) : the_post(); ?>
		<header class="mb-10">
			<h1 class="font-display uppercase text-4xl md:text-6xl"><?php the_title(); ?></h1>
		</header>
		<div class="prose prose-lg max-w-none prose-headings:font-display prose-headings:uppercase prose-a:text-usam-volt">
			<?php the_content(); ?>
		</div>
	<?php endwhile; ?>
</article>

<?php get_footer();
