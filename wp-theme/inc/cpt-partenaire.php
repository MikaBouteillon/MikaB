<?php
/**
 * Custom Post Type : Partenaire / Sponsor.
 */

defined( 'ABSPATH' ) || exit;

add_action( 'init', function () {
	register_post_type( 'partenaire', [
		'labels' => [
			'name'          => __( 'Partenaires', 'usam' ),
			'singular_name' => __( 'Partenaire', 'usam' ),
			'add_new'       => __( 'Ajouter un partenaire', 'usam' ),
			'edit_item'     => __( 'Modifier le partenaire', 'usam' ),
			'menu_name'     => __( 'Partenaires', 'usam' ),
		],
		'public'         => true,
		'show_in_rest'   => true,
		'has_archive'    => false,
		'menu_icon'      => 'dashicons-awards',
		'menu_position'  => 23,
		'supports'       => [ 'title', 'editor', 'thumbnail' ],
		'rewrite'        => [ 'slug' => 'partenaire' ],
	] );

	register_taxonomy( 'categorie_partenaire', 'partenaire', [
		'labels' => [
			'name'          => __( 'Catégories de partenaires', 'usam' ),
			'singular_name' => __( 'Catégorie', 'usam' ),
		],
		'public'            => true,
		'hierarchical'      => true,
		'show_in_rest'      => true,
		'show_admin_column' => true,
	] );

	register_post_meta( 'partenaire', 'usam_partenaire_url', [
		'show_in_rest'  => true,
		'single'        => true,
		'type'          => 'string',
		'auth_callback' => function() { return current_user_can( 'edit_posts' ); },
	] );
} );
