<?php
/**
 * Custom Post Type : Joueur.
 *
 * Permet de créer une fiche joueur dans WP-Admin avec :
 *  - nom (titre)
 *  - photo (image mise en avant)
 *  - poste, numéro, équipe (taxonomies / champs custom via ACF ou bloc)
 *  - bio (contenu)
 */

defined( 'ABSPATH' ) || exit;

add_action( 'init', function () {
	register_post_type( 'joueur', [
		'labels' => [
			'name'               => __( 'Joueurs', 'usam' ),
			'singular_name'      => __( 'Joueur', 'usam' ),
			'add_new'            => __( 'Ajouter un joueur', 'usam' ),
			'add_new_item'       => __( 'Ajouter un nouveau joueur', 'usam' ),
			'edit_item'          => __( 'Modifier le joueur', 'usam' ),
			'new_item'           => __( 'Nouveau joueur', 'usam' ),
			'view_item'          => __( 'Voir le joueur', 'usam' ),
			'search_items'       => __( 'Rechercher un joueur', 'usam' ),
			'not_found'          => __( 'Aucun joueur trouvé', 'usam' ),
			'menu_name'          => __( 'Joueurs', 'usam' ),
		],
		'public'              => true,
		'has_archive'         => false,
		'show_in_rest'        => true,
		'menu_icon'           => 'dashicons-businessperson',
		'menu_position'       => 21,
		'supports'            => [ 'title', 'editor', 'thumbnail', 'excerpt', 'page-attributes' ],
		'rewrite'             => [ 'slug' => 'joueur' ],
	] );

	register_taxonomy( 'equipe', 'joueur', [
		'labels' => [
			'name'          => __( 'Équipes', 'usam' ),
			'singular_name' => __( 'Équipe', 'usam' ),
		],
		'public'            => true,
		'hierarchical'      => true,
		'show_in_rest'      => true,
		'show_admin_column' => true,
	] );

	register_taxonomy( 'poste', 'joueur', [
		'labels' => [
			'name'          => __( 'Postes', 'usam' ),
			'singular_name' => __( 'Poste', 'usam' ),
		],
		'public'            => true,
		'hierarchical'      => false,
		'show_in_rest'      => true,
		'show_admin_column' => true,
	] );
} );
