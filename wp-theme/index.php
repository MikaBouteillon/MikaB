<?php
/**
 * Fallback — utilisé si aucun template plus spécifique ne matche.
 */
defined( 'ABSPATH' ) || exit;

get_header(); ?>

<section class="container mx-auto px-4 lg:px-8 py-16">
	<?php if ( have_posts() ) : ?>
		<div class="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
			<?php while ( have_posts() ) : the_post(); ?>
				<article class="bg-white border border-usam-slate-200">
					<?php if ( has_post_thumbnail() ) : ?>
						<a href="<?php the_permalink(); ?>" class="block aspect-video overflow-hidden">
							<?php the_post_thumbnail( 'usam-card', [ 'class' => 'w-full h-full object-cover' ] ); ?>
						</a>
					<?php endif; ?>
					<div class="p-6">
						<h2 class="font-display uppercase text-xl mb-2">
							<a href="<?php the_permalink(); ?>" class="hover:text-usam-volt"><?php the_title(); ?></a>
						</h2>
						<p class="text-sm text-usam-slate-700 mb-4"><?php echo esc_html( get_the_date() ); ?></p>
						<?php the_excerpt(); ?>
					</div>
				</article>
			<?php endwhile; ?>
		</div>

		<div class="mt-12">
			<?php the_posts_pagination( [
				'mid_size'  => 1,
				'prev_text' => '←',
				'next_text' => '→',
			] ); ?>
		</div>
	<?php else : ?>
		<p><?php esc_html_e( 'Aucun contenu pour le moment.', 'usam' ); ?></p>
	<?php endif; ?>
</section>

<?php get_footer();
