<?php
/**
 * Enregistrement des menus WordPress.
 */

defined( 'ABSPATH' ) || exit;

add_action( 'after_setup_theme', function () {
	register_nav_menus( [
		'primary' => __( 'Menu principal', 'usam' ),
		'footer'  => __( 'Menu pied de page', 'usam' ),
		'legal'   => __( 'Mentions légales (footer bas)', 'usam' ),
	] );
} );
