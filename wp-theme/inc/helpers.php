<?php
/**
 * Helpers utilisés dans les templates.
 */

defined( 'ABSPATH' ) || exit;

/**
 * Récupère le prochain match d'une équipe donnée (slug taxonomie equipe).
 *
 * @param string $equipe_slug Slug de l'équipe (ex: green-team).
 * @return WP_Post|null
 */
function usam_get_next_match( string $equipe_slug = 'green-team' ): ?WP_Post {
	$today = current_time( 'Y-m-d' );

	$q = new WP_Query( [
		'post_type'      => 'match_usam',
		'posts_per_page' => 1,
		'meta_key'       => 'usam_match_date',
		'orderby'        => 'meta_value',
		'order'          => 'ASC',
		'meta_query'     => [
			[
				'key'     => 'usam_match_date',
				'value'   => $today,
				'compare' => '>=',
				'type'    => 'DATE',
			],
			[
				'key'     => 'usam_match_equipe',
				'value'   => $equipe_slug,
				'compare' => '=',
			],
		],
	] );

	return $q->have_posts() ? $q->posts[0] : null;
}

/**
 * Affiche un CTA Volt.
 */
function usam_cta( string $label, string $url, string $variant = 'primary' ): void {
	$base    = 'inline-flex items-center justify-center px-6 py-3 font-display tracking-wide uppercase text-sm transition';
	$variants = [
		'primary'   => 'bg-usam-volt text-usam-charcoal hover:bg-usam-yellow',
		'secondary' => 'border border-usam-volt text-usam-volt hover:bg-usam-volt hover:text-usam-charcoal',
		'ghost'     => 'text-usam-volt underline-offset-4 hover:underline',
	];
	$class = $base . ' ' . ( $variants[ $variant ] ?? $variants['primary'] );

	printf(
		'<a class="%s" href="%s">%s</a>',
		esc_attr( $class ),
		esc_url( $url ),
		esc_html( $label )
	);
}
