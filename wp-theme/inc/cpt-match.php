<?php
/**
 * Custom Post Type : Match.
 *
 * Une rencontre = un post. Champs principaux gérés via meta.
 */

defined( 'ABSPATH' ) || exit;

add_action( 'init', function () {
	register_post_type( 'match_usam', [
		'labels' => [
			'name'          => __( 'Matchs', 'usam' ),
			'singular_name' => __( 'Match', 'usam' ),
			'add_new'       => __( 'Ajouter un match', 'usam' ),
			'add_new_item'  => __( 'Ajouter un match', 'usam' ),
			'edit_item'     => __( 'Modifier le match', 'usam' ),
			'menu_name'     => __( 'Matchs', 'usam' ),
		],
		'public'         => true,
		'show_in_rest'   => true,
		'has_archive'    => true,
		'menu_icon'      => 'dashicons-calendar-alt',
		'menu_position'  => 22,
		'supports'       => [ 'title', 'editor', 'thumbnail' ],
		'rewrite'        => [ 'slug' => 'matchs' ],
	] );
} );

// Champs meta pour un match (date, adversaire, score, lieu, équipe USAM concernée)
add_action( 'init', function () {
	$fields = [ 'usam_match_date', 'usam_match_adversaire', 'usam_match_lieu',
	            'usam_match_score_usam', 'usam_match_score_adv', 'usam_match_competition',
	            'usam_match_equipe', 'usam_match_billetterie_url' ];

	foreach ( $fields as $key ) {
		register_post_meta( 'match_usam', $key, [
			'show_in_rest'  => true,
			'single'        => true,
			'type'          => 'string',
			'auth_callback' => function() { return current_user_can( 'edit_posts' ); },
		] );
	}
} );
